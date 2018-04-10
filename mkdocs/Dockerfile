FROM python:alpine3.6

LABEL maintainer="pcrespov" \
      description="mkdocs - project documentation with markdown"

WORKDIR /usr/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /usr/app
EXPOSE 8000

ENTRYPOINT [ "python", "-m", "mkdocs" ]

# http://www.mkdocs.org/
#  MkDocs - Project documentation with Markdown.
#
#Options:
#  -V, --version  Show the version and exit.
#  -q, --quiet    Silence warnings
#  -v, --verbose  Enable verbose output
#  -h, --help     Show this message and exit.
#
#Commands:
#  build      Build the MkDocs documentation
#  gh-deploy  Deploy your documentation to GitHub Pages
#  new        Create a new MkDocs project
#  serve      Run the builtin development server

CMD ["serve", "--dev-addr", "0.0.0.0:8000", "--livereload" ]
