import React from 'react';
import $ from 'jquery';

// const MessageParser = ({ children, actions }) => {
//   const parse = (message) => {
//     console.log(message);
//   };

//   return (
//     <div>
//       {React.Children.map(children, (child) => {
//         return React.cloneElement(child, {
//           parse: parse,
//           actions: {},
//         });
//       })}
//     </div>
//   );
// };

// export default MessageParser;
class MessageParser {
  constructor(actionProvider) {
    this.actionProvider = actionProvider;
  }

  parse(message) {
    const stuff = message.toLowerCase()

    fetch('/App', 
    {
      method: 'POST',
      body: JSON.stringify({string: stuff}),
      headers: { 'Content-Type': 'application/json' },
    });
    
    
    // if (stuff.includes("hello")) {
    //   this.actionProvider.greet()
    // }
  }
}

export default MessageParser
