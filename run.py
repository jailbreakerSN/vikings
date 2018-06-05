from app import create_app

# app.config.from_object('config.BaseConfig')
app = create_app()

if __name__ == '__main__':
    app.run(port=5002, debug=False)
