import { Container, Group } from '@mantine/core';
import React, { useState, useEffect } from 'react';


const endpoints = [
  'http://165.22.80.193:8000',
  'http://165.22.80.193:8001',
  'http://165.22.80.193:8002',
  'http://165.22.80.193:8003',
];

async function fetchCardData() {
  const cardData = [];

  for (let i = 0; i < endpoints.length; i++) {
    try {
      const response = await fetch(endpoints[i]);
      const data = await response.json();
      const card = {
        id: i + 1,
        name: `Agent ${i + 1}`,
        address: data.state.address,
        status: data.state.round,
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
    fetchCardData().then((data) => {
      setCardData(data);
    });
  }, []);

  return (
    <Container size="lg">
      <Group position="center" grow>
        {cardData.map((card) => (
          <div key={card.id} className="border border-gray-300 rounded-md p-4">
            <h1 className="text-xl font-semibold">{card.name}</h1>
            <p>{card.address}</p>
            <p>{card.status}</p>
          </div>
        ))}
      </Group>
    </Container>
  );
};


export default Hero;