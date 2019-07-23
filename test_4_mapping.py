from typing import List, Dict


def map_framework_to_language(languages: List[str], frameworks: List[str]) -> Dict[str, str]:
    """ map the given framework to the related language.
    The framework will be mapped to the language which is at the same index.
    example:
    languages = ['php', 'ruby', 'python', 'python']
    frameworks = ['symfony', 'Ruby on Rails', 'django', 'zope']
    return: {'php': ['symfony'], 'ruby': ['Ruby on Rails'], 'python': ['django',
    'zope']}
    :param list languages: list of languages to associate
    :param list frameworks: list of frameworks to associate
    :return: map of languages and their frameworks
    :rtype: dict
    """
    mapping = {}
    for i, language in enumerate(languages):
        # we could optimize the code by ignoring the if test and the assignment
        # See the next function: map_setdefault_framework_to_language()
        if language not in mapping:
            mapping[language] = []
        mapping[language].append(frameworks[i])
    return mapping


def map_setdefault_framework_to_language(languages: List[str], frameworks: List[str]) -> Dict[str, str]:
    mapping = {}
    for i, language in enumerate(languages):
        mapping.setdefault(language, []).append(frameworks[i])
    return mapping


if __name__ == "__main__":
    languages = ['php', 'ruby', 'python', 'python']
    frameworks = ['symfony', 'Ruby on Rails', 'django', 'zope']

    res_actual_map = map_framework_to_language(languages=languages, frameworks=frameworks)
    print(res_actual_map)

    print("we could optimize the code by ignoring the if test and the assignment")
    res_dict_map = map_setdefault_framework_to_language(languages=languages, frameworks=frameworks)
    print(res_dict_map)
