#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from GithubWrapper import GithubWrapper
from GitlabWrapper import GitlabWrapper
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

user = GithubWrapper()

############################################
# Index
############################################

@app.route('/', methods=['GET'])
def index_route():
    return jsonify({
        'author': 'code-monk08',
        'author_url': 'https://code-monk08.github.io/',
        'base_url': '',
        'project_name': 'Generic API Wrapper',
        'project_url': 'https://github.com/alice-sieve/Open-Source/tree/API-Wrapper-code-monk08',
        })


###########################################
# GET ORGANIZATIONS/ GROUP MEMBERS
###########################################

#github
@app.route('/<platform>/orgs/<org>/members', methods=['GET'])
def get_org_members_route(platform, org):

    # GET github/orgs/:org/members
    if platform == "github":
        result = dict(user.get_org_members(org))
        return jsonify(result)

#gitlab
@app.route('/<platform>/groups/<group_id>/members', methods=['GET'])
def get_group_members_route(platform, group_id):
    
    # GET gitlab/groups/:id/members
    if platform == "gitlab":
        result = dict(GitlabWrapper.get_group_members(group_id))
        return jsonify(result)


###########################################
# GET ORGANIZATIONS REPOS/ GROUP PROJECTS 
###########################################

#github
@app.route('/<platform>/orgs/<org>/repos', methods=['GET'])
def get_org_repos_route(platform, org):
    
    # GET github/orgs/:org/repos
    if platform == "github":
        result = dict(user.get_org_repos(org))
        return jsonify(result)

#gitlab
@app.route('/<platform>/groups/<group_id>/projects', methods=['GET'])
def get_group_projects_route(platform, group_id):
    
    # GET gitlab/groups/:id/projects
    if platform == "gitlab":
        result = dict(GitlabWrapper.get_group_projects(group_id))
        return jsonify(result)


###########################################
# GET REPOS COMMITS / PROJECTS COMMITS 
###########################################

#github
@app.route('/<platform>/repos/<owner>/<repo>/commits', methods=['GET'])
def get_repo_commits_route(platform, owner, repo):
    
    # GET github/repos/:owner/:repo/commits
    if platform == "github":
        result = dict(user.get_repo_commits(str(owner+"/"+repo)))
        return jsonify(result)

#gitlab
@app.route('/<platform>/projects/<project_id>/repository/commits', methods=['GET'])
def get_project_commits_route(platform, project_id):
    
    # GET gitlab/projects/:id/repository/commits
    if platform == "gitlab":
        result = dict(GitlabWrapper.get_project_commits(project_id))
        return jsonify(result)

###########################################
# GET REPOS ISSUES / PROJECTS ISSUES 
###########################################

#github
@app.route('/<platform>/repos/<owner>/<repo>/issues', methods=['GET'])
def get_repo_issues_route(platform, owner, repo):
    
    # GET github/repos/:owner/:repo/issues
    if platform == "github":
        result = dict(user.get_repo_issues(str(owner+"/"+repo)))
        return jsonify(result)

#gitlab
@app.route('/<platform>/projects/<project_id>/issues', methods=['GET'])
def get_project_issues_route(platform, project_id):
    
    # GET gitlab/projects/:id/issues
    if platform == "gitlab":
        result = dict(GitlabWrapper.get_project_issues(project_id))
        return jsonify(result)

###########################################
# GET ORGANIZATION ISSUES / GROUPS ISSUES 
###########################################

#github
@app.route('/<platform>/orgs/<org>/issues', methods=['GET'])
def get_org_issues_route(platform, org):
    
    # GET github/orgs/:org/issues
    if platform == "github":
        result = dict(user.get_org_issues(org))
        return jsonify(result)

#gitlab
@app.route('/<platform>/groups/<group_id>/issues', methods=['GET'])
def get_group_issues_route(platform, group_id):
    
    # GET gitlab/groups/:id/issues
    if platform == "gitlab":
        result = dict(GitlabWrapper.get_group_issues(group_id))
        return jsonify(result)

##################################################
# GET REPO ISSUES COMMENTS/ PROJECT ISSUE COMMENTS   
##################################################

#github
@app.route('/<platform>/repos/<owner>/<repo>/issues/comments', methods=['GET'])
def get_issue_comments_route(platform, owner, repo):
    
    # GET github/repos/:owner/:repo/issues/comments
    if platform == "github":
        result = dict(user.get_issue_comments_dict(str(owner+"/"+repo)))
        return jsonify(result)

#gitlab
@app.route('/<platform>/projects/<project_id>/issues/<issue_iid>/notes', methods=['GET'])
def get_issue_comments_dict_route(platform, project_id, issue_iid):
    
    # GET gitlab/projects/:id/issues/:issue_iid/notes
    if platform == "gitlab":
        result = dict(GitlabWrapper.get_issue_comments_dict(project_id, issue_iid))
        return jsonify(result)


##################################################
# GET REPO PULL REQUESTS / PROJECT MERGE REQUESTS   
##################################################

#github
@app.route('/<platform>/repos/<owner>/<repo>/pulls', methods=['GET'])
def get_repo_pulls_route(platform, owner, repo):
    
    # GET github/repos/:owner/:repo/pulls
    if platform == "github":
        result = dict(user.get_repo_pulls(str(owner+"/"+repo)))
        return jsonify(result)

#gitlab
@app.route('/<platform>/projects/<project_id>/merge_requests', methods=['GET'])
def get_project_merge_request_route(platform, project_id):
    
    # GET gitlab/projects/:id/merge_requests
    if platform == "gitlab":
        result = dict(GitlabWrapper.get_project_merge_request(project_id))
        return jsonify(result)

###########################################
# Start Flask
###########################################

if __name__ == '__main__':
    app.run()