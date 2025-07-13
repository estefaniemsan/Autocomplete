import React from "react";
import './SearchBar.css'
import { GoSearch } from "react-icons/go";
import { IconContext } from "react-icons";
import {useEffect, useState } from 'react'
import { AiOutlineClose } from "react-icons/ai";
import axios from "axios";


function SearchBar() {

    const [inputs, setinputs] = useState("")
    const [filters, setfilters] = useState([])

    const API = process.env.REACT_APP_API_URL || "http://localhost:4000";
    const handleFilter = async (event) => {
    const query = event.target.value;
    setinputs(query);

    if (query === "") {
        setfilters([]);
        return;
    }

    try {
       
        let res = await axios.get(`${API}/autocomplete?q=${query}`);
        let resultados = res.data.map((title, idx) => ({ id: idx, title }));

      

       
        if (resultados.length === 0) {
            await axios.post(`${API}/autocomplete/scrape`, { base: query })
            res = await axios.get(`${API}/autocomplete?q=${query}`);
            resultados = res.data.map((title, idx) => ({ id: idx, title }));
        }

        setfilters(resultados);
        } catch (error) {
        console.error("Erro ao buscar sugestões:", error);
        setfilters([]);
        }
    };


    useEffect(() => {

        if (inputs === "") {
            setfilters([])
        }

    }, [inputs])

    function handleClickAutoComplete(value) {
        setinputs(value.title)
        setfilters([])
    }

    function cleartext(){
        setinputs("")
        setfilters([])
    }

    return (
                <div style={{ position: 'relative', width: '500px' }}>
        <div className="searchInput">
            <IconContext.Provider value={{ color: "blue", size: "30px" }}>
            <GoSearch />
            <input value={inputs} onChange={handleFilter} type="text" placeholder="Pesquisar..." />
            {inputs !== "" ? <AiOutlineClose onClick={cleartext} /> : ""}
            </IconContext.Provider>
        </div>

        {filters.length !== 0 &&
            <div className='dataResult'>
            {filters.map(value => (
                <div key={value.id} className="dataItem" onClick={() => handleClickAutoComplete(value)} >
                <IconContext.Provider value={{ color: "blue", size: "22px" }}>
                    <GoSearch />
                </IconContext.Provider>
                <p>{value.title}</p>
                </div>
            ))}
            </div>
        }
        </div>
    )
        
    
}

export default SearchBar;
