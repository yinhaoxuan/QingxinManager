import React, {Component} from 'react'
import axios from "axios";
import ItemDisplay from "./ItemDisplay";
import Api from './Api'
import TopBar from "./TopBar";

class Article extends Component {
    state = {
        data: {
            authors: [],
            editor: {},
            department: {},
        }
    }

    componentDidMount() {
        Api.get_article(this.props.match.params.id).then(res => {
            const {data} = res.data
            console.log(data)
            this.setState({data})
        })
    }

    render() {
        return (
            <div>
                <TopBar/>
                <div>
                    <h1>{this.state.data.title}</h1>
                    <p>作者：{this.state.data.authors.map((author) => {
                        return <ItemDisplay Data={author} Type='person' key={author.id}/>
                    })}</p>
                    <p>责编：<ItemDisplay Data={this.state.data.editor} Type='person'/></p>
                    <p>部门：<ItemDisplay Data={this.state.data.department} Type='department'/></p>
                    <p>{this.state.data.content}</p>
                </div>
            </div>
        )
    }
}

export default Article
