import github_loader

app = github_loader.create_app()

if __name__ == '__main__':
    app.run(debug=True)
