import { createChatBotMessage } from 'react-chatbot-kit';

const config = {
  initialMessages: [createChatBotMessage(`Hi! How can I help you today?`)],
  floating: true,
  botAvatar: "icon.png",
  customStyles: {
    botMessageBox: {
      backgroundColor: '#16b8ba',
    },
    chatButton: {
      backgroundColor: '#007511',
    },
  },

};

export default config;
