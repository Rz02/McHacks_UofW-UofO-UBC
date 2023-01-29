//to run, go to cmd of this directory and do `npm start`

/*
To shut, type `netstat -ano | findstr :<PORT>` 
then run taskkill /PID <PID> /F
where PID is the last number to the right
*/


import Chatbot from 'react-chatbot-kit'
import 'react-chatbot-kit/build/main.css'
import config from './config.js';
import MessageParser from "./MessageParser.js";
import ActionProvider from './ActionProvider.js';

const App = () => {
  return (
    <div class="app">
      <h1>Student Budget Planner!</h1>
      <Chatbot
        config={config}
        messageParser={MessageParser}
        actionProvider={ActionProvider}
      />
    </div>
  );
};
export default App;
