
function Footer() {
  return (
    <footer className="border-top text-center small text-muted py-3">
      <p>
      
          Home
  
        |{" "}
          About Us

        |{" "}

          Terms

      </p>
      <p className="m-0">
        Copyright &copy; {new Date().getFullYear()}{" "}

          ComplexApp
        
        . All rights reserved.
      </p>
    </footer>
  )
}

export default Footer
