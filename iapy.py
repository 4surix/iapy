# coding: utf-8
# Python 3.6.2
# ----------------------------------------------------------------------------


__version__ = '0.0.1'


def alias(__alias__:dict = {}, **alias):

    alias = {**__alias__, **alias}

    alias_params = {
        alias: arg
        for arg, alias in alias.items()
        for alias in ([alias] if isinstance(alias, str) else alias)
    }

    alias_attrs = {
        arg: ([alias] if isinstance(alias, str) else alias)
        for arg, alias in alias.items()
    }

    def __convert_function(function):

        def __function(*args, **kwargs):
            return function(*args, **{
                alias_params.get(kwarg, kwarg): value
                for kwarg, value in kwargs.items()
            })

        return __function

    def __convert_attr(__object__, identifier, identifier_alias):

        setattr(
            __object__, 
            identifier_alias,
            property(
                lambda self: getattr(self, identifier)
            ).setter(
                lambda self, value: setattr(self, identifier, value)
            )
        )

    def __recover_object(__object__):

        function = type(__recover_object)

        if isinstance(__object__, function):

            return __convert_function(__object__)

        elif isinstance(__object__, type):

            for item in dir(__object__):

                value = getattr(__object__, item)

                if isinstance(value, function):
                    setattr(__object__, item, __convert_function(value))

            for identifier, identifiers_alias in alias_attrs.items():

                for identifier_alias in identifiers_alias:

                    if identifier == identifier_alias:
                        continue

                    __convert_attr(__object__, identifier, identifier_alias)

        elif isinstance(__object__, dict):

            __object__.update(
                {
                    identifier_alias: __object__[identifier]
                    for identifier, identifiers_alias in alias_attrs.items()
                    for identifier_alias in identifiers_alias
                    if identifier in __object__
                }
            )

        else:
            raise ValueError(f"Type '{type(__object__).__name__}' not supported.")

        return __object__

    return __recover_object