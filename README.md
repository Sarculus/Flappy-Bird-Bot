# Personal IP

## Dependencies
### Client
Install dependencies:
```
cd client
npm install
```
### Domain
Install libraries:

```
pip install Pillow
pip install numpy
pip install mss
pip install pywin32
pip install redis
```
install FastAPI and Uvicorn:
```
pip install fastapi
pip install uvicorn
```
Make sure to install to the correct path. If installed to an alternative path make sure to add this path to the windows environment variables (system and user)
***

## Build Commands
### Client

Run the Vite server:
```
cd client
npm run dev
```
### Domain
Run the Uvicorn server:
```
uvicorn domain.api.main:app --reload
```
***

## Project Goals
The goal of the project is to create a gameplay bot, specifically for the game Flappy Bird.
***


## Software Stack
### Frontend
- Language: TypeScript
- Server: Vite
- Typescript framework: Vue
- Design tool: Webflow + HTML/CSS
### Backend
- Language: Python
- Server: Uvicorn
- API framework: FastAPI
- Unit testing: Pytest
- CI: Gitlab CI
- Database: Redis
***


## Resources
- [Vite: Get started](https://vitejs.dev/guide/)
- [FastAPI: Installation](https://fastapi.tiangolo.com/#installation)
- [Webflow](https://webflow.com)
- [Pytest: Get started](https://docs.pytest.org/en/8.2.x/getting-started.html)
- [Redis: Install on windows](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/)
***