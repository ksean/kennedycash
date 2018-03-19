import React, { Component } from 'react';

class App extends Component {
    state = {
        personalTransactions: []
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/api/');
            const personalTransactions = await res.json();
            this.setState({
                personalTransactions
            });
        } catch (e) {
            console.log(e);
        }
    }

    render() {
        return (
            <div>
                {this.state.personalTransactions.map(item => (
                    <div key={item.id}>
                        <span>{item.date} </span>
                        <span>{item.description} </span>
                        <span>{item.amount}</span>
                    </div>
                ))}
            </div>
        );
    }
}

export default App;