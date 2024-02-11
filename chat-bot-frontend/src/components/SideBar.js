import React, { useState, useContext, useEffect } from 'react';
import { MdChevronLeft, MdChevronRight, MdClearAll } from 'react-icons/md';
import { ChatContext } from '../context/chatContext';
import logo from '../assets/logo.png';

const SideBar = () => {
  const [open, setOpen] = useState(true);
  const [, , clearMessages] = useContext(ChatContext);
  const [modalOpen, setModalOpen] = useState(false);

  function handleResize() {
    window.innerWidth <= 720 ? setOpen(false) : setOpen(true);
  }

  useEffect(() => {
    handleResize();
  }, []);

  const clearChat = () => clearMessages();

  return (
    <section className={` ${open ? 'w-screen lg:w-96' : 'w-16'} sidebar bg-zinc-800 text-white`}>
      <div className="sidebar__app-bar">
        <div className="flex items-center">
          <div className={`sidebar__app-logo ${!open && 'scale-0 hidden'}`}>
            <span className="w-8 h-8">
              <img width="30" src={logo} alt="Logo" />
            </span>
          </div>
          <h1 className={`sidebar__app-title ${!open && 'scale-0 hidden'}`}>SAGE</h1>
        </div>
        <div className={'sidebar__btn-close'} onClick={() => setOpen(!open)}>
          {open ? (
            <MdChevronLeft className="text-white sidebar__btn-icon" />
          ) : (
            <MdChevronRight className="text-white sidebar__btn-icon" />
          )}
        </div>
      </div>
      <div className="nav">
        <span className="border nav__item border-neutral-600" onClick={clearChat}>
          <div className="nav__icons text-white">
            <MdClearAll />
          </div>
          <h1 className={`${!open && 'hidden'} text-white`}>Clear chat</h1>
        </span>
      </div>
    </section>
  );
};

export default SideBar;
