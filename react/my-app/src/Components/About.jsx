import React, { useState } from 'react';
import './About.css';

const About = () => {

    return (
        <p>
            This site allows comparison between photos of people and determining whether it is the same person, a matter that is a significant challenge in any legal or criminal investigation.
            <br />
            Different developed software helps the law authorities to determine with high probability the chances of identification (identity) between images.
            <br />
            Comparison results of certain software are even accepted as admissible legal evidence. <br />
            The development proposed here is intended to give the common citizen tools similar to those in the hands of the authorities in order to give peace of mind and calmness and allow immediate and accessible help for everyone. <br />
            The website will compare the photos that the user uploads from all possible angles and return the level of probability that it is indeed the same person or not.
        </p>
    );
};

export default About;

