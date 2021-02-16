import {Component} from "react";
import {AppBar, Button, Chip, Link, Toolbar, Typography} from "@material-ui/core";

class TopBar extends Component {
    render() {
        return (
            <div>
                <AppBar position="static">
                    <Toolbar>
                        <Button href='#/' color='inherit'>清新时报稿件管理系统</Button>
                    </Toolbar>
                </AppBar>
            </div>
        );
    }
}

export default TopBar