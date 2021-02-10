import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import axios from "axios";

class App extends React.Component {
    state = {
        departments: [],
        persons: [],
        articles: [],
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/person_list')
    }
}