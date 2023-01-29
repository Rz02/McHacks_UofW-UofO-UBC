import { createChatBotMessage } from 'react-chatbot-kit';



const config = {
  initialMessages: [createChatBotMessage('Hi! How can I help you today?')],
  floating: true,
  botName: "BudgetBot",
  customStyles: {
    botAvatar :{
      img: "icon.png",
    },
    botMessageBox: {
      backgroundColor: '#16b8ba',
    },
    chatButton: {
      backgroundColor: '#007511',
    },
  
  },

};

export default config;
