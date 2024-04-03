{
    presets: [
      "@vue/cli-plugin-babel/preset", // Ensure this exists
      ["@vue/babel-preset-jsx", {
        "injectH": false // Optional, to avoid automatic 'h' function creation
      }]
    ]
  };

