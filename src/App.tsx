import { ReactComponent as IconMenu } from './logo.svg'
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                {/* <img src={logo} className="App-logo" alt="logo" /> */}
                <IconMenu width="200" />
                <p>
                    We moved:
                </p>
                <a
                    className="App-link"
                    href="https://simonwardjones.co.uk"
                    target="simonwardjones.co.uk"
                >
                    simonwardjones.co.uk
                </a>
            </header>
        </div>
    );
}

export default App;
