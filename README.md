
# WebSocket Web chat with aiohttp and aioredis

Web chat application with aiohttp which utilises co-routines and WebSockets

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
- Redis on loclahost

## Usage
Run server 'python main.py'


1. Open browser
2. enter: http://localhost:8080
3. Click connect

## File descriptions:
1. main.py: Contans server logic and routes. Application initialization with redis
2. view.py: Websockets initializations
3. template/index.html: Displays current user, all users in chatroom, sending and display all messages.

## Built With

* [Docker](http://www.docker.com/) - Contrainer engine
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Sergey Leksikov** - *author* 
See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

