import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Main from './Main';
import Router from "./Router";

ReactDOM.render(
    <React.StrictMode>
        <Router/>
    </React.StrictMode>,
    document.getElementById('root')
);

