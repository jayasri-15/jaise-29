import logo from './logo.svg';
import './App.css';
import CricketScore from './components/CricketScore';

function App() {
  return (
    <div>
      <CricketScore target={200} totalOvers={10}  />
      <br></br>
    </div>
  );
}

export default App;
