import React, { useEffect, useRef } from 'react';
import Draggable from 'react-draggable';

const QuizModal = ({ quiz, onAnswer }) => {
    const nodeRef = useRef(null);

    useEffect(() => {
        if (quiz) {
            console.log('QuizModal: Opening with new quiz.');
        } else {
            
        }
    }, [quiz]);

    if (!quiz) return null;

    return (
        <Draggable nodeRef={nodeRef} handle=".quiz-modal-handle">
            <div ref={nodeRef} className="quiz-modal-overlay">
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