import React, {Component} from 'react'
import axios from "axios";

class Article extends Component {
    state = {
        data: {
            authors: [],
            editor: {},
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/get_article', {
            params: {
                id: this.props.match.params.id
            }
        })
            .then(res => {
                const {data} = res.data
                console.log(data)
                this.setState({data})
            })
    }

    render() {
        return (
            <div>
                <h1>{this.state.data.title}</h1>
                <p>{"作者：" + this.state.data.authors.map((author) => {
                    return author.name
                })}</p>
                <p>{"责编：" + this.state.data.editor.name}</p>
                <p>{this.state.data.content}</p>
            </div>
        )
    }
}

export default Article