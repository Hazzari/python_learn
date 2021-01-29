from app import app

# # Два варианта создания конфига

# app.config.update(DEBUG=True)
app.config.from_object('config.DevelopmentConfig')

if __name__ == '__main__':
    app.run()
