from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'techinenergystorage'  # <storage_account_name>
    account_key = 'pyMniIi+LmM4fgQ/ZiusqORiBc7jCRlsTfy4cS2gKD7ePKbC3j9U65W+eDrmGRJZCIfsRe35stC4+AStSJfMRg=='  # <storage_account_key>
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = 'techinenergystorage'  # <storage_account_name>
    account_key = 'pyMniIi+LmM4fgQ/ZiusqORiBc7jCRlsTfy4cS2gKD7ePKbC3j9U65W+eDrmGRJZCIfsRe35stC4+AStSJfMRg=='  # <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
