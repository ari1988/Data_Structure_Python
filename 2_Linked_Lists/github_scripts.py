## Get user details from token
import requests,json
headers = {
    'Authorization': 'token {{ACCESS_TOKEN}}'
}

url = "https://api.github.com/user"

response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))

##===============================================##
## Create a repo
import requests,json
headers = {
    'Authorization': 'token {{ACCESS_TOKEN}}',
    'Accept': 'application/vnd.github.v3+json'
}

url = 'https://api.github.com/user/repos'

data = json.dumps({
    'name': 'adofirst1',
    'description': 'Repo created via API'
})

response = requests.post(url, headers=headers, data=data)
print(json.dumps(response.json(), indent=4))

## Parameters of creating a repository

## name : This is the repository’s name.
## description : This is the repository’s description.
## homepage : This is the repository’s information URL.
## private : This is true if the repository is private.
## visibility : This indicates whether a repository is private or public.
## has_issues : This is true if issues are enabled and false if issues are disabled.
## has_projects : This is true if projects are enabled and false if projects are disabled.
## has_wiki : This is true if wiki is enabled and false if wiki is disabled.
## is_template : This is true if the repository can be made as a template repository and false if it can’t be.
## auto_init : This is true if we want to make a commit on an empty README file.
## gitignore_template : This is the name of the template required for the desired platform or language.
## license_template : This is any suitable license template.
## allow_squash_merge : This is true if squash merge is enabled and false if squash merge is disabled.
## allow_merge_commit : This is true if merge commit is enabled and false if merge commit is disabled.
## allow_rebase_merge : This is true if rebase merge is enabled and false if rebase merge is disabled.
## allow_auto_merge : This is true if auto merge is enabled and false if auto merge is disabled.
## delete_branch_on_merge : This is true if the delete branch on merge is enabled and false if the delete branch on merge is disabled.

##===============================================##
## List Repositories
headers = {
    'Authorization': 'token {{ACCESS_TOKEN}}',
    'Accept': 'application/vnd.github.v3+json'
}

url = "https://api.github.com/users/ari1988/repos"

response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))

##===============================================##
## Update a repository name
headers = {
    'Authorization': 'token {{ACCESS_TOKEN}}',
    'Accept': 'application/vnd.github.v3+json'
}

data = json.dumps({
    'name': 'adofirst2'
})

url = "https://api.github.com/repos/ari1988/adofirst1"

response = requests.patch(url, headers=headers, data=data)
print(json.dumps(response.json(), indent=4))

##===============================================##
## Remove a repository
headers = {
    'Authorization': 'token {{ACCESS_TOKEN}}',
    'Accept': 'application/vnd.github.v3+json'
}

url = 'https://api.github.com/repos/ari1988/adofirst2'

response = requests.delete(url, headers=headers)

if response.status_code == 204:
    print('The repository was deleted successfully.')
elif response.status_code == 307:
    print('There has been a redirect temporarily.')
else:
    print('The repository we were looking for was not found.')

##===============================================##
## List branches
    headers = {
    'Authorization': 'token {{ACCESS_TOKEN}}',
    'Accept': 'application/vnd.github.v3+json'
}

url = 'https://api.github.com/repos/ari1988/Data_Structure_Python/branches'

response = requests.get(url)
print(json.dumps(response.json(), indent=4))
##===============================================##
## Get a branch
headers = {
    'Authorization': 'token {{ACCESS_TOKEN}}',
    'Accept': 'application/vnd.github.v3+json'
}

url = 'https://api.github.com/repos/ari1988/adofirst1/branches/<branch-name>'

response = requests.get(url)
print(json.dumps(response.json(), indent=4))

##===============================================##
## Rename a branch
headers = {
    'Authorization': 'token {{ACCESS_TOKEN}}',
    'Accept': 'application/vnd.github.v3+json'
}

url = 'https://api.github.com/repos/ari1988/adofirst1/branches/<branch-name>/rename'

data = json.dumps({
    'new_name': 'develop'
})

response = requests.post(url, headers=headers, data=data)
print(json.dumps(response.json(), indent=4))
##===============================================##
## Merge a branch
# base : This specifies the name of the branch that the head will be merged into.
# head : This specifies the branch name or a commit SHA1 to be merged.
# commit_message : This is the message used when a merge commit occurs. If no message is specified, the default message is used.

headers = {
    'Authorization': 'token {{ACCESS_TOKEN}}',
    'Accept': 'application/vnd.github.v3+json'
}

url = 'https://api.github.com/repos/ari1988/adofirst1/merges'

data = json.dumps({
    'base': '<base-name>',
    'head': '<head-name>'
})

response = requests.post(url, headers=headers, data=data)
print(json.dumps(response.json(), indent=4))