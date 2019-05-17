//frontend/src/app.js
import React, { Component } from 'react';

class App extends Component {
  state = {
    notices: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://backendj.run.goorm.io/api/notices');
      const notices = await res.json();
      this.setState({
        notices
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.notices.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.content}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
