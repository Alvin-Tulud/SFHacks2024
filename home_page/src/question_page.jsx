import React, { useState } from 'react';
import {createRoot} from 'react-dom/client';
import './index.css';

const Questionnaire = () => {
  const [questions, setQuestions] = useState([
    {
      id: 1,
      question: 'What is your name?',
      type: 'text',
    },
    {
      id: 2,
      question: 'What is your age?',
      type: 'number',
    },
    {
      id: 3,
      question: 'What is your gender?',
      type: 'radio',
      options: ['Male', 'Female', 'Other'],
    },
  ]);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setQuestions((prevQuestions) => {
      const updatedQuestions = prevQuestions.map((question) => {
        if (question.id === name) {
          return {
            ...question,
            answer: value,
          };
        }
        return question;
      });
      return updatedQuestions;
    });
  };

  const handleSubmit = () => {
    // Submit the questionnaire data to a backend server
  };

  return (
    <div>
      <h1>Questionnaire</h1>
      <form onSubmit={handleSubmit}>
        {questions.map((question) => (
          <div key={question.id}>
            <label htmlFor={question.id}>{question.question}</label>
            <input
              type={question.type}
              id={question.id}
              name={question.id}
              value={question.answer}
              onChange={handleInputChange}
            />
          </div>
        ))}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

const root = createRoot(document.getElementById('mbti'));
root.render(
  <React.StrictMode>
    <Questionnaire />
  </React.StrictMode>
);