import React, { useEffect } from 'react';
import Draggable from 'react-draggable';

const QuizModal = ({ quiz, onAnswer }) => {
    useEffect(() => {
        if (quiz) {
            console.log('QuizModal: Opening with new quiz.');
        } else {
            console.log('QuizModal: Closing.');
        }
    }, [quiz]);

    if (!quiz) return null;

    return (
        <Draggable handle=".quiz-modal-handle">
            <div className="quiz-modal-overlay">
                <div className="quiz-modal">
                    <div className="quiz-modal-handle">Drag from here</div>
                    <h2>{quiz.question}</h2>
                    <div className="quiz-answers">
                        {quiz.answers.map((answer, index) => (
                            <button key={index} onClick={() => onAnswer(index)} className="btn">
                                {answer}
                            </button>
                        ))}
                    </div>
                </div>
            </div>
        </Draggable>
    );
};

export default QuizModal;
