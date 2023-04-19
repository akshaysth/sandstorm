#!/usr/bin/python
import os
import re
import warnings
from datetime import datetime

from frontmatter import Frontmatter

warnings.filterwarnings('ignore')


def edit():
    for mdfile in os.listdir('_posts/'):
        path = f"./_posts/{mdfile}"
        date = datetime.fromtimestamp(os.stat(path).st_ctime).strftime("%Y-%m-%d %H:%M:%S -0400")
        post = Frontmatter.read_file(path)

        if not post.get('frontmatter'):
            filename = path.split('/')[-1].split('.')[0].split('-')
            title_str = ' '.join(filename[3:]).capitalize()

            yaml = f"---\ntitle: {title_str}\nlayout: post\ndate: {date}\ncategories: data\ntags: jekyll update\n---\n\n"
            with open(path, 'r') as file:
                filedata = file.read()
                filedata = re.sub(r"!\[png\]\(", "<img src=\"/assets/images/", filedata)
                filedata = re.sub(r".png\)", ".png\">", filedata)
                filedata = yaml + filedata
                with open(path, 'w') as file:
                    file.write(filedata)


if __name__ == '__main__':
    edit()
