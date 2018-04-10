# mkdocs dockerfile

[mkdocs] renders all markdown into a website. The configuration is given by ```mkdocs.yml``` and build a website.

Example of usage:

```bash
    cd mkdocs
    docker-compose build
    docker-compose run mkdocs --help

    # creates a new mkdocs project
    docker-compose run mkdocs new .

    # serves in localhost:8000 and auto-updates with changes in markdown source
    docker-compose run --service-ports mkdocs

    # stops everything
    docker-compose down
```

```bash
    # serves in localhost:8000 and auto-updates with changes in markdown source
    docker run -d -v $(pwd):/usr/app  -p 8000:8000 itisfoundation/mkdocs
```

#### TODO

- [ ] Change user so generator does not create files as root

[mkdocs]:http://www.mkdocs.org/
