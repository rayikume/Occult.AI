import { useState } from "react";
import ChatboxCSS from "./Chatbox.module.css";
import ChatIcon from "../../Assets/ChatIcon.svg";
import aniLoader from "../../Assets/aniLoader.svg";
import axios from "axios";

interface Message {
  role: "user" | "assistant";
  content: string;
}

const Chatbox = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState<string>("");
  const [isChatbotVisible, setIsChatbotVisible] = useState<boolean>(false);
  const [isProcessing, setIsProcessing] = useState<boolean>(false);

  const handleSend = async () => {
    if (!input.trim()) {
      return;
    }

    const userMessage: Message = { role: "user", content: input };
    setMessages([...messages, userMessage]);
    setInput("");
    setIsProcessing(true);

    try {
      const response = await axios.post("http://127.0.0.1:8000/query", {
        prompt: input,
      });
      console.log(response);
      const botMessage: Message = {
        role: "assistant",
        content: response.data,
      };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
      setIsProcessing(false);
    } catch (error) {
      alert(`Error fetching chatbot response: ${error}`);
      setIsProcessing(false);
    }
  };

  const toggleChatbotVisibility = () => {
    setIsChatbotVisible(!isChatbotVisible);
  };

  return (
    <>
      <div className={ChatboxCSS.chatlogo_container}>
        <img
          src={ChatIcon}
          className={ChatboxCSS.chatbotIcon}
          onClick={toggleChatbotVisibility}
        />
      </div>
      {isChatbotVisible && (
        <div className={ChatboxCSS.chatbox_container}>
          <div className={ChatboxCSS.chatbot_title}>AI ChatBot</div>
          <div className={ChatboxCSS.chatbox}>
            <div className={ChatboxCSS.messages}>
              <div className={`${ChatboxCSS.message} ${ChatboxCSS.assistant}`}>
                Hello 👋, I am the AI ChatBot! I'm here to help you with
                anything you're looking for. Please provide your descriptions
                below and I'll show the relative content.
              </div>
              {messages.map((msg, index) => (
                <div
                  key={index}
                  className={`${ChatboxCSS.message} ${
                    msg.role === "user" ? ChatboxCSS.user : ChatboxCSS.assistant
                  }`}
                >
                  {msg.content}
                </div>
              ))}
              {isProcessing && (
                <div
                  className={`${ChatboxCSS.message} ${ChatboxCSS.assistant}`}
                >
                  <img src={aniLoader} />
                </div>
              )}
            </div>
            <div className={ChatboxCSS.input_container}>
              <input
                type="text"
                value={input}
                className={ChatboxCSS.prompt_input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && handleSend()}
              />
              <button className={ChatboxCSS.prompt_submit} onClick={handleSend}>
                Send
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default Chatbox;
