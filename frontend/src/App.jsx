import './App.css'
import {Routes, Route} from 'react-router-dom'
import ArrayPage from './pages/ArrayPage.jsx'
import BSTPage from './pages/BSTPage.jsx'
import DLLPage from './pages/DLLPage.jsx'
import HashmapPage from './pages/HashmapPage.jsx'
import HomePage from './pages/HomePage.jsx'
import QueuePage from './pages/QueuePage.jsx'
import SLLPage from './pages/SLLPage.jsx'
import AlgorithmsPage from './pages/AlgorithmsPage.jsx'
import StackPage from './pages/StackPage.jsx'

function App() {
  return (
    <Routes>
      <Route path="/" element = {<HomePage />} />
      <Route path="/algorithms" element = {<AlgorithmsPage />} />

      <Route path="/structures/array" element = {<ArrayPage />} />
      <Route path="/structures/bst" element = {<BSTPage />} />
      <Route path="/structures/dll" element = {<DLLPage />} />
      <Route path="/structures/hashmap" element = {<HashmapPage />} />
      <Route path="/structures/queue" element = {<QueuePage />} />
      <Route path="/structures/sll" element = {<SLLPage />} />
      <Route path="/structures/stack" element = {<StackPage />} />

    </Routes>
  )
}

export default App
