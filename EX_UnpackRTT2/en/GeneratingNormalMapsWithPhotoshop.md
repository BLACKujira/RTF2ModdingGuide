# Generating Normal Maps with Photoshop

Many older or low-spec platform games, including *R-Type Tactics II*, do not use normal maps. If you import these models into *R-Type Final 2*, the smooth surfaces may look unnatural.

Here’s a simple method for generating basic normal maps using *Photoshop* and the *color/diffuse texture*.  
Since I'm still relatively new to 3D modeling, there might be better approaches, but this method works reasonably well.

## Steps

1. Open the *color texture* in *Photoshop*
2. Go to `Filter` -> `3D` -> `Generate Normal Map`
3. Adjust the parameters and click OK

- The resulting normal map won't be highly accurate—it only simulates basic depth—but it’s often sufficient to enhance surface details.

# Other Tips

To compensate for the lack of normal maps and post-processing, *R-Type Tactics II*’s color textures contain heavy baked-in shadows. These can look excessive when imported into *R-Type Final 2*. You can reduce this effect with filters, or even repaint certain elements like cockpits.

Also, *R-Type Tactics II* textures are quite small, so they'll appear blurry in *R-Type Final 2*. Consider using upscaling algorithms or AI tools to improve resolution.
