import { Container, Group } from '@mantine/core';
import React, { useState, useEffect } from 'react';


const endpoints = [
  'http://165.22.80.193:8000',
  'http://165.22.80.193:8001',
  'http://165.22.80.193:8002',
  'http://165.22.80.193:8003',
];

function truncate(str, n){
  return (str.length > n) ? str.slice(0, n-1) + '&hellip;' : str;
};


async function fetchCardData() {
  const cardData = [];

  for (let i = 0; i < endpoints.length; i++) {
    try {
      const response = await fetch(endpoints[i]);
      const data = await response.json();
      const card = {
        id: i + 1,
        name: `Agent ${i + 1}`,
        address: truncate(data.state.address, 20),
        status: data.state.round,
        link: "https://polygonscan.com/address/" + data.state.address
      };
      cardData.push(card);
    } catch (error) {
      console.error('Error fetching data from API:', error);
    }
  }

  return cardData;
}

fetchCardData().then((cardData) => {
  console.log(cardData);
});


const Hero = () => {
  const [cardData, setCardData] = useState([]);

  useEffect(() => {
  const intervalId = setInterval(() => {
    fetchCardData().then((data) => {
      setCardData(data);
    });
    }, 1000);
  }, []);

  return (
    <Container size="lg">
      <Group position="center" grow>
        {cardData.map((card) => (
          <div key={card.id} className="border border-gray-300 rounded-md p-4">
            <h1 className="text-xl font-semibold">{card.name}</h1>
            <a href={card.link}>
                <p>{card.address}</p>
            </a>
            <p>{card.status}</p>
          </div>
        ))}
      </Group>
    </Container>
  );
};


export default Hero;