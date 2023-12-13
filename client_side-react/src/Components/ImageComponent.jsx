import React from 'react';

class ImageComponent extends React.Component {
  render() {
    const { imageUrl } = this.props;
    return (
      <div>
        <img src={imageUrl} alt="תמונה" />
      </div>
    );
  }
}

export default ImageComponent;
