const obj = {
    "რიგი_0": [2, 4, 6, 8, 10],
    "რიგი_1": [1, 3, 5, 7, 9]   
  };
  
  for (let i = 0; i < Math.min(obj["რიგი_0"].length, obj["რიგი_1"].length); i++) {
    console.log(`რიგი_0: ${obj["რიგი_0"][i]}, რიგი_1: ${obj["რიგი_1"][i]}`);
  }