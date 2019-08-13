#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from GithubWrapper import GithubWrapper
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
        'project_name': 'Github API Wrapper',
        'project_url': '',
        })


############################################
# GitHub
###########################################

# GET /users/:username

# @app.route('/users/<username>', methods=['GET'])
# def get_user_name_route(username):
#     result = dict(user.get_user_name(username))
#     return jsonify(date=result['date'], sunsign=result['sunsign'],
#                    horoscope=result['horoscope'])


# GET /orgs/:org/members

@app.route('/orgs/<org>/members', methods=['GET'])
def get_org_members_route(org):
    result = dict(user.get_org_members(org))
    return jsonify(result)


# GET /orgs/:org/repos

@app.route('/orgs/<org>/repos', methods=['GET'])
def get_org_repos_route(org):
    result = dict(user.get_org_repos(org))
    return jsonify(result)


# GET /repos/:owner/:repo/commits

@app.route('/repos/<owner>/<repo>/commits', methods=['GET'])
def get_repo_commits_route(owner, repo):
    result = dict(user.get_repo_commits(str(owner+"/"+repo)))
    return jsonify(result)


# GET /repos/:owner/:repo/issues

@app.route('/repos/<owner>/<repo>/issues', methods=['GET'])
def get_repo_issues_route(owner, repo):
    result = dict(user.get_repo_issues(str(owner+"/"+repo)))
    return jsonify(result)


# GET /orgs/:org/issues

@app.route('/orgs/<org>/issues', methods=['GET'])
def get_org_issues_route(org):
    result = dict(user.get_org_issues(org))
    return jsonify(result)


# GET /repos/:owner/:repo/issues/comments

@app.route('/repos/<owner>/<repo>/issues/comments', methods=['GET'])
def get_issue_comments_route(owner, repo):
    result = dict(user.get_issue_comments_dict(str(owner+"/"+repo)))
    return jsonify(result)


# GET /repos/:owner/:repo/pulls

@app.route('/repos/<owner>/<repo>/pulls', methods=['GET'])
def get_repo_pulls_route(owner, repo):
    result = dict(user.get_repo_pulls(str(owner+"/"+repo)))
    return jsonify(result)

###########################################
# Start Flask
###########################################

if __name__ == '__main__':
    app.run()