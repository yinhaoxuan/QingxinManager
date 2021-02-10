import React from 'react'
import {HashRouter, Route, Switch} from "react-router-dom";
import App from "./App";
import Article from "./Article";

const BasicRoute = () => {
    return (
        <HashRouter>
            <Switch>
                <Route exact path='/' component={App}/>
                <Route exact path='/article/:id' component={Article}/>
            </Switch>
        </HashRouter>
    )
}

export default BasicRoute