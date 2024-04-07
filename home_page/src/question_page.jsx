import React, { useState } from 'react';
import {createRoot} from 'react-dom/client';
import './index.css';

const Questionnaire = () => {
  const [questions, setQuestions] = useState([
    {
        id: 1,
        question: 'What is your gender?',
        type: 'radio',
        options: ['gooner', 'balls'],
    },
    {
        id: 2,
        question: 'What is your gender?',
        type: 'radio',
        options: ['gooner', 'balls'],
    },
    {
      id: 3,
      question: 'What is your gender?',
      type: 'radio',
      options: ['gooner', 'balls'],
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
            <h3>{question.question}</h3>
            <label htmlFor={question.id}>{question.options[0]}</label>
            <input
              type={'radio'}
              id={question.id}
              name={question.id}
              value={question.options[2]}
              onChange={handleInputChange}
              required
            />
            <label htmlFor={question.id}>{question.options[1]}</label>
            <input
              type={'radio'}
              id={question.id}
              name={question.id}
              value={question.options[1]}
              onChange={handleInputChange}
              required
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