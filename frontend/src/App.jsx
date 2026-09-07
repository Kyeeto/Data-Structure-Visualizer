import './App.css'
import {Routes, Route, NavLink} from 'react-router-dom'
import ArrayPage from './pages/ArrayPage.jsx'
import BSTPage from './pages/BSTPage.jsx'
import DLLPage from './pages/DLLPage.jsx'
import HashmapPage from './pages/HashmapPage.jsx'
import HomePage from './pages/HomePage.jsx'
import NotFoundPage from './pages/NotFoundPage.jsx'
import QueuePage from './pages/QueuePage.jsx'
import SLLPage from './pages/SLLPage.jsx'
import AlgorithmsPage from './pages/AlgorithmsPage.jsx'
import StackPage from './pages/StackPage.jsx'


function App() {
  return (
    <>
      <header>
        <h1>Data Structure and Algorithm Visualizer</h1>
      </header>

      <div className = "app-layout">
        <nav>
          <NavLink to="/">Home</NavLink>
          <NavLink to="/algorithms">Algorithms</NavLink>
          <NavLink to="/structures/array">Array</NavLink>
          <NavLink to="/structures/bst">Binary Search Tree</NavLink>
          <NavLink to="/structures/dll">Doubly Linked List</NavLink>
          <NavLink to="/structures/hashmap">Hashmap</NavLink>
          <NavLink to="/structures/queue">Queue</NavLink>
          <NavLink to="/structures/sll">Singly Linked List</NavLink>
          <NavLink to="/structures/stack">Stack</NavLink>
        </nav>
      </div>

      <main>
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
          <Route path="*" element ={<NotFoundPage />} />

        </Routes>
      </main>

      <footer>

      </footer>
    </>
  )
}

export default App
