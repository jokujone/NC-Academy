import React, { useState, useEffect } from 'react';
interface Person {
    name: string;
    address: string;
    country: string;
}

export default function Persons() {
    const [data, setData] = useState<Person[]>([])
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");


    useEffect(() => {
        fetch('https://localhost:7170/api/persons')
            .then((response) => {
                if (!response.ok) {
                    throw new Error('We are doomed');
                }
                return response.json();
            })
            .then((json) => {
                setData(json);
                setLoading(false);
            })
            .catch((err) => {
                setError(err.name + " " + err.message + " " + err.stack);
                setLoading(false);
            });
    }, []);


    if (loading) return <p>Loading...</p>;
    if (error) return <p>OH MY GOD: {error}</p>;


    return (
        <>
            <h1>Persons</h1>
            <ul>
                {data && data.map((person: Person) => (
                    <li key={person.name}>{person.name}, {person.address}, {person.country}</li>
                ))}
            </ul>
        </>
    )
}