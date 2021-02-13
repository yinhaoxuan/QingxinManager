import React from 'react'
import {HashRouter, Route, Switch} from "react-router-dom";
import Main from "./Main";
import Article from "./Article";
import Person from "./Person";
import Department from "./Department";

const BasicRoute = () => {
    return (
        <HashRouter>
            <Switch>
                <Route exact path='/' component={Main}/>
                <Route exact path='/article/:id' component={Article}/>
                <Route exact path='/person/:id' component={Person}/>
                <Route exact path='/department/:id' component={Department}/>
            </Switch>
        </HashRouter>
    )
}

export default BasicRoute