def slugify(string='', separator='_', to_lower=False):
    if to_lower:
        string = string.lower()
    validator = {
        'ə':'e', 'ö':'o', 'ü':'u','ı':'i', 'ğ':'g', 'ş':'s', 'ç':'c',
        'Ə':'E', 'Ö':'O', 'Ü':'U','I':'İ', 'Ğ':'G', 'Ş':'S', 'Ç':'C'
        }
    for key in validator:
        if key in string:
            string = string.replace(key, validator[key])
    string = string.split()
    return separator.join(string)