#!/bin/bash

# Usage:  $0  blog_url ipython_notebook_file blog_title 

# Transforms an ipython notebook into html and post it on tumblr as a draft blog post


if [ "$#" -lt 3 ]; then
    echo "Usage: $0 blog_url ipython_notebook_file blog_title "
    exit 1
fi

# Rads parameters
blog_url=$1
ipnb_file=$2
blog_title="$3"


# Deals with space in filename
new_ipnb_file=$(echo $ipnb_file | sed -e 's/ /\ /g')

# Converts ipython notebook into html file
ipython nbconvert --to html "$new_ipnb_file"

# Generate filename output from ipython nbconvert
filename=$(basename "$new_ipnb_file")
filename="${filename%.*}"
extension=".html"
html_file=$filename$extension

# Execute the python script
python post_ipnb.py -i "$html_file" -t "$blog_title"

echo "Done"
