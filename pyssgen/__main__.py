#!/usr/bin/env python3

import os
import sys
from jinja2 import Environment, FileSystemLoader
import frontmatter
import markdown
from slugify import slugify


def checkargs():
    '''
        checks command line arguments
        params: none
        return: True for success, False for failure
    '''
    global INPUT_FOLDER
    global DIST_FOLDER
    global TEMPLATE_FOLDER
    if len(sys.argv) == 1:
        print("█▀▀█ █░░█ █▀▀ █▀▀ █▀▀▀ █▀▀ █▀▀▄")
        print("█░░█ █▄▄█ ▀▀█ ▀▀█ █░▀█ █▀▀ █░░█")
        print("█▀▀▀ ▄▄▄█ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀░░▀\n")
        print("Python Static Site Generator by Kenneth Soares")
        print("usage: ./main.py <IN_DIR> <OUT_DIR> (<TEMP_DIR>)")
        return False
    elif len(sys.argv) < 3:
        print("missing arguments!")
        print("for help: ./main.py")
        return False
    elif len(sys.argv) == 4:
        INPUT_FOLDER = sys.argv[1]
        DIST_FOLDER = sys.argv[2]
        TEMPLATE_FOLDER = sys.argv[3]
    else:
        INPUT_FOLDER = sys.argv[1]
        DIST_FOLDER = sys.argv[2]
        TEMPLATE_FOLDER = "./templates"
    return True

def load_input():
    '''
       creates a list of all the posts in input directory
       params: none
       return: posts: list
    '''
    posts = [f for f in os.listdir(INPUT_FOLDER)]
    return posts

def process_posts(posts):
    '''
        creates a dict with all of the metadata and content for each post
        params: posts: list
        return: post_data: dict
    '''
    posts_data = []
    for post in posts:
        with open(f"{INPUT_FOLDER}/{post}", "r") as f:
            file_data = frontmatter.load(f)
            metadata = file_data.metadata
            metadata["slug"] = slugify(metadata["title"])

            # we're creating "type" fields so that we can have other types
            # of posts like videos and whatnot
            metadata["type"] = "post"
            content = markdown.markdown(file_data.content,extensions=['fenced_code','tables'])
            posts_data.append({"metadata": metadata, "content":content})
    return posts_data

def render_templates(posts_data,env):
    '''
        renders home template as html
        params: posts_data: list, env:jinja2.environment.Environment
        return: 0 if success
    '''
    template = env.get_template("home.html")
    all_metadata = [data["metadata"] for data in posts_data]
    all_metadata.sort(key=lambda x: x["date"], reverse=True)

    renderer_template = template.render(data=all_metadata)
    os.makedirs(DIST_FOLDER, exist_ok=True)
    with open(f"{DIST_FOLDER}/index.html", "w") as f:
        f.write(renderer_template)
    return 0

def render_posts(posts_data,env):
    '''
        renders posts as html
        params: posts_data: list, env:jinja2.environment.Environment
        return: 0 if success
    '''
    for data in posts_data:
        type = data["metadata"]["type"]
        template = env.get_template(f"{type}.html")
        rendered_template = template.render(data=data)
        os.makedirs(f"dist/{type}", exist_ok=True)
        with open(f"dist/{type}/{data['metadata']['slug']}.html", 'w') as f:
            f.write(rendered_template)
    return 0

def copy_static():
    '''
        copy static files into dist folder
        params: none
        return: 0 if success
    '''
    os.makedirs("dist/static", exist_ok=True)
    for file in os.listdir("static"):
        with open(f"static/{file}", "r") as f:
            with open(f"dist/static/{file}", "w") as f2:
                f2.write(f.read())
    return 0


if __name__ == "__main__":
    print("fucking shit")
    if not checkargs():
        exit(1)
    posts = load_input()
    posts_data = process_posts(posts)
    env = Environment(loader=FileSystemLoader(TEMPLATE_FOLDER))
    render_templates(posts_data,env)
    render_posts(posts_data,env)
    copy_static()
