SUBJECTS = ["nsubj", "nsubjpass", "csubj", "csubjpass", "agent", "expl"]
OBJECTS = ["dobj", "dative", "attr", "oprd"]


def get_subs_from_conjunctions(subs):
    more_subs = []
    for sub in subs:
        # rights is a generator
        rights = list(sub.rights)
        right_deps = {tok.lower_ for tok in rights}
        if "and" in right_deps:
            more_subs.extend(
                [tok for tok in rights if tok.dep_ in SUBJECTS or tok.pos_ == "NOUN"])
            if len(more_subs) > 0:
                more_subs.extend(get_subs_from_conjunctions(more_subs))
    return more_subs


def get_objects_from_conjunctions(objs):
    more_objs = []
    for obj in objs:
        # rights is a generator
        rights = list(obj.rights)
        right_deps = {tok.lower_ for tok in rights}
        if "and" in right_deps:
            more_objs.extend(
                [tok for tok in rights if tok.dep_ in OBJECTS or tok.pos_ == "NOUN"])
            if len(more_objs) > 0:
                more_objs.extend(get_objects_from_conjunctions(more_objs))
    return more_objs


def get_verbs_from_conjunctions(verbs):
    more_verbs = []
    for verb in verbs:
        right_deps = {tok.lower_ for tok in verb.rights}
        if "and" in right_deps:
            more_verbs.extend(
                [tok for tok in verb.rights if tok.pos_ == "VERB"])
            if len(more_verbs) > 0:
                more_verbs.extend(get_verbs_from_conjunctions(more_verbs))
    return more_verbs


def find_subs(tok):
    head = tok.head
    while head.pos_ != "VERB" and head.pos_ != "NOUN" and head.head != head:
        head = head.head
    if head.pos_ == "VERB":
        subs = [tok for tok in head.lefts if tok.dep_ == "SUB"]
        if len(subs) > 0:
            verb_negated = is_negated(head)
            subs.extend(get_subs_from_conjunctions(subs))
            return subs, verb_negated
        elif head.head != head:
            return find_subs(head)
    elif head.pos_ == "NOUN":
        return [head], is_negated(tok)
    return [], False


def is_negated(tok):
    negations = {"no", "not", "n't", "never", "none"}
    for dep in list(tok.lefts) + list(tok.rights):
        if dep.lower_ in negations:
            return True
    return False


def find_svs(tokens):
    svs = []
    verbs = [tok for tok in tokens if tok.pos_ == "VERB"]
    for v in verbs:
        subs, verb_negated = get_all_subs(v)
        if len(subs) > 0:
            for sub in subs:
                svs.append(
                    (sub.orth_, "!" + v.orth_ if verb_negated else v.orth_))
    return svs


def get_objs_from_prepositions(deps):
    objs = []
    for dep in deps:
        if dep.pos_ == "ADP" and dep.dep_ == "prep":
            objs.extend([tok for tok in dep.rights if tok.dep_ in OBJECTS or (
                tok.pos_ == "PRON" and tok.lower_ == "me")])
    return objs


def get_objs_from_attributes(deps):
    for dep in deps:
        if dep.pos_ == "NOUN" and dep.dep_ == "attr":
            verbs = [tok for tok in dep.rights if tok.pos_ == "VERB"]
            if len(verbs) > 0:
                for v in verbs:
                    rights = list(v.rights)
                    objs = [tok for tok in rights if tok.dep_ in OBJECTS]
                    objs.extend(get_objs_from_prepositions(rights))
                    if len(objs) > 0:
                        return v, objs
    return None, None


def get_obj_from_open_clausal_complement(deps):
    for dep in deps:
        if dep.pos_ == "VERB" and dep.dep_ == "xcomp":
            v = dep
            rights = list(v.rights)
            objs = [tok for tok in rights if tok.dep_ in OBJECTS]
            objs.extend(get_objs_from_prepositions(rights))
            if len(objs) > 0:
                return v, objs
    return None, None


def get_all_subs(v):
    verb_negated = is_negated(v)
    subs = [tok for tok in v.lefts if tok.dep_ in SUBJECTS and tok.pos_ != "DET"]
    if len(subs) > 0:
        subs.extend(get_subs_from_conjunctions(subs))
    else:
        found_subs, verb_negated = find_subs(v)
        subs.extend(found_subs)
    return subs, verb_negated


def get_all_objs(v):
    # rights is a generator
    rights = list(v.rights)
    objs = [tok for tok in rights if tok.dep_ in OBJECTS]
    objs.extend(get_objs_from_prepositions(rights))

    # TODO: check this
    # potential_new_verb, potential_new_objs = get_objs_from_attributes(rights)
    # if potential_new_verb is not None and potential_new_objs is not None and len(potential_new_objs) > 0:
    #    objs.extend(potential_new_objs)
    #    v = potential_new_verb

    potential_new_verb, potential_new_objs = get_obj_from_open_clausal_complement(
        rights)
    if potential_new_verb is not None and potential_new_objs is not None and len(potential_new_objs) > 0:
        objs.extend(potential_new_objs)
        v = potential_new_verb
    if len(objs) > 0:
        objs.extend(get_objects_from_conjunctions(objs))
    return v, objs


def find_svos(tokens):
    svos = []
    verbs = [tok for tok in tokens if tok.pos_ == "VERB" and tok.dep_ != "aux"]
    for v in verbs:
        subs, verb_negated = get_all_subs(v)
        # hopefully there are subs, if not, don't examine this verb any longer
        if len(subs) > 0:
            v, objs = get_all_objs(v)
            for sub in subs:
                for obj in objs:
                    obj_negated = is_negated(obj)
                    svos.append(
                        (sub.lower_, "!" + v.lower_ if verb_negated or obj_negated else v.lower_, obj.lower_))
    return svos
