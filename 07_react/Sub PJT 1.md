# Sub PJT 1

## 개발 환경 구성

### 1. Chocolatey

- Package Installer
- Powershell (run as administrator)

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

### 2. Node.js 

1. node -v 인스톨 여부 확인

2. #### 미설치시 choco install nodejs

3. node -v , npm -v 

### 3. VSCODE

 1. #### choco install vscode

 2. #### Extensions

     	1. ESLint
     	2. ES7 React/Redux/GraphQL/React-Native Snippets
     	3. Prettier
     	4. Rainbow Brackets

### 4. Chrome extensions - React Dev Tools

## CRA

#### create-react-app

- #### cra 설치

```bash
npm install -g create-react-app
```

- 폴더 경로 내에 cra를 실행하여 `<app-name>`  생성

```bash
npx create-react-app react-base
```

- 해당경로 이동후 react 실행

```bash
cd .\react-base\
npm start
```



위포트 신헌의 psat for ncs 수리 자료해석

위포트 ncs  하주응 문제해결 자료해석 

에듀얼 / 위포트 통합 기본서

