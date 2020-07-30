import React, { Component } from "react";
import ReactDOM from "react-dom";
import * as THREE from "three";
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'

export default class App extends Component {
  componentDidMount() {
    // === THREE.JS CODE START ===
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );
    var geometry = new THREE.BoxGeometry( 1, 1, 1 );
    var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
    var cube = new THREE.Mesh( geometry, material );

    var loader = new GLTFLoader()
    
    loader.load('bone3.glb', (gltf) => {
      debugger
      scene.add(gltf.scene)
    }, undefined, function(error){
      console.log(error)
    })

    camera.position.z = 5;
    // === THREE.JS EXAMPLE CODE END ===
  }
  render() {
    return (
      <div ref={ref => (this.mount = ref)} />
    )
  }
}